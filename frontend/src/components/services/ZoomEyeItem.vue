<template>
  <div class="block content is-normal" v-if="queries.length > 0">
    <h4 class="is-size-4">
      <span class="icon">
        <img src="https://www.google.com/s2/favicons?domain=www.zoomeye.org" alt="zoomeye" />
      </span>
      ZoomEye
      <span class="icon" @click="toggleIsHidden()">
        <font-awesome-icon icon="caret-down" v-if="isHidden" />
        <font-awesome-icon icon="caret-up" v-else />
      </span>
    </h4>
    <QueryTags :queries="queries" v-if="!isHidden" />
  </div>
</template>

<script setup lang="ts">
import { useToggle } from "@vueuse/core"
import { computed, type PropType, ref } from "vue"

import QueryTags from "@/components/services/QueryTags.vue"
import type { Fingerprint, Query } from "@/types"

const props = defineProps({
  fingerprint: {
    type: Object as PropType<Fingerprint>,
    required: true
  }
})

const isHidden = ref(true)

const toggleIsHidden = useToggle(isHidden)

const createLink = (query: string): string => {
  const baseUrl = "https://www.zoomeye.org/searchResult?q="
  return baseUrl + encodeURI(query)
}

const queries = computed<Query[]>(() => {
  const q: Query[] = []

  if (props.fingerprint.favicon) {
    const query = `iconhash:"${props.fingerprint.favicon.mmh3}"`
    q.push({ key: "Favicon", query: query, link: createLink(query) })
  }

  if (props.fingerprint.certificate) {
    const query = `ssl.cert.fingerprint:"${props.fingerprint.certificate.sha1}"`
    q.push({ key: "Certificate", query: query, link: createLink(query) })
  }

  return q
})
</script>
