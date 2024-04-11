<script setup lang="ts">
import { useToggle } from "@vueuse/core"
import qs from "qs"
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
  const baseUrl = "https://onyphe.io/search/?"
  const params = {
    query
  }
  return baseUrl + qs.stringify(params)
}

const queries = computed<Query[]>(() => {
  const q: Query[] = [
    {
      key: "HTML",
      query: `category:datascan app.http.bodymd5:"${props.fingerprint.html.md5}"`,
      link: createLink(`category:datascan app.http.bodymd5:"${props.fingerprint.html.md5}"`)
    }
  ]

  if (props.fingerprint.favicon) {
    const query = `category:datascan app.favicon.imagemmh3:"${props.fingerprint.favicon?.mmh3}"`
    q.push({ key: "Favicon", query: query, link: createLink(query) })
  }

  return q
})
</script>

<template>
  <div class="block content is-normal">
    <h4 class="is-size-4">
      <span class="icon">
        <img src="https://www.google.com/s2/favicons?domain=onyphe.io" alt="shodan" />
      </span>
      Onyphe
      <span class="icon" @click="toggleIsHidden()">
        <font-awesome-icon icon="caret-down" v-if="isHidden" />
        <font-awesome-icon icon="caret-up" v-else />
      </span>
    </h4>
    <QueryTags :queries="queries" v-if="!isHidden" />
  </div>
</template>
