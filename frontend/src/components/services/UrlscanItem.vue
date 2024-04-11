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
  const baseUrl = "https://urlscan.io/search/#"
  return baseUrl + encodeURI(query)
}

const queries = computed<Query[]>(() => {
  const q: Query[] = [
    {
      key: "HTML",
      query: `hash:${props.fingerprint.html.sha256}`,
      link: createLink(props.fingerprint.html.sha256)
    }
  ]

  if (props.fingerprint.favicon) {
    q.push({
      key: "Favicon",
      query: `hash:${props.fingerprint.favicon.sha256}`,
      link: createLink(props.fingerprint.favicon.sha256)
    })
  }

  ;(props.fingerprint.dns.a || []).forEach((record) => {
    const query = `page.ip:${record.host}`
    q.push({ key: "A", query: record.host, link: createLink(query) })
  })

  return q
})
</script>

<template>
  <div class="block content is-normal">
    <h4 class="is-size-4">
      <span class="icon">
        <img src="https://www.google.com/s2/favicons?domain=urlscan.io" alt="shodan" />
      </span>
      urlscan.io
      <span class="icon" @click="toggleIsHidden()">
        <font-awesome-icon icon="caret-down" v-if="isHidden" />
        <font-awesome-icon icon="caret-up" v-else />
      </span>
    </h4>
    <QueryTags :queries="queries" v-if="!isHidden" />
  </div>
</template>
