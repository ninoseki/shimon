<script setup lang="ts">
import { useToggle } from "@vueuse/core"
import { Base64 } from "js-base64"
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

const base64fy = (s: string) => {
  return Base64.encode(s).trim()
}

const createLink = (q: string): string => {
  const baseUrl = "https://en.fofa.info/result?"
  const qbase64 = base64fy(q)
  const params = { qbase64 }
  return baseUrl + qs.stringify(params)
}

const queries = computed<Query[]>(() => {
  const q: Query[] = [
    {
      key: "Title",
      query: `title="${props.fingerprint.html.title}"`,
      link: createLink(`title="${props.fingerprint.html.title}"`)
    }
  ]

  if (props.fingerprint.favicon) {
    const query = `icon_hash="${props.fingerprint.favicon?.mmh3}"`
    q.push({
      key: "Favicon",
      query: query,
      link: createLink(query)
    })
  }

  if (props.fingerprint.tls) {
    const query = `jarm="${props.fingerprint.tls.jarm}"`
    q.push({
      key: "JARM",
      query: query,
      link: createLink(query)
    })
  }

  return q
})
</script>

<template>
  <div class="block content is-normal">
    <h4 class="is-size-4">
      <span class="icon">
        <img src="https://www.google.com/s2/favicons?domain=fofa.info" alt="fofa" />
      </span>
      Fofa
      <span class="icon" @click="toggleIsHidden()">
        <font-awesome-icon icon="caret-down" v-if="isHidden" />
        <font-awesome-icon icon="caret-up" v-else />
      </span>
    </h4>
    <QueryTags :queries="queries" v-if="!isHidden" />
  </div>
</template>
