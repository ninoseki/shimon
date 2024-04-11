<template>
  <div class="block content is-normal" v-if="queries.length > 0">
    <h4 class="is-size-4">
      <span class="icon">
        <img src="https://www.google.com/s2/favicons?domain=virustotal.com" alt="vt" />
      </span>
      VirusTotal
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
  return `https://www.virustotal.com/gui/ip-address/${query}/detail`
}

const createVTILink = (query: string): string => {
  return `https://www.virustotal.com/gui/search/${query}/urls`
}

const queries = computed<Query[]>(() => {
  const q: Query[] = (props.fingerprint.dns.a || []).map((record) => {
    return { key: "A", query: record.host, link: createLink(record.host) }
  })

  if (props.fingerprint.favicon) {
    const query = `entity:url main_icon_md5:${props.fingerprint.favicon.md5}`
    q.push({
      key: "Favicon",
      query: query,
      link: createVTILink(query)
    })
  }

  return q
})
</script>
