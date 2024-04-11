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

const createLink = (q: string): string => {
  const baseUrl = "https://search.censys.io/search?"
  const resource = "hosts"
  const params = {
    q,
    resource
  }
  return baseUrl + qs.stringify(params)
}

const queries = computed<Query[]>(() => {
  const q: Query[] = [
    {
      key: "HTML",
      query: `services.http.response.body_hash:"sha1:${props.fingerprint.html.sha1}"`,
      link: createLink(`services.http.response.body_hash:"sha1:${props.fingerprint.html.sha1}"`)
    }
  ]

  if (props.fingerprint.html.title) {
    const query = `services.http.response.html_title:"${props.fingerprint.html.title}"`
    q.push({ key: "Title", query: query, link: createLink(query) })
  }

  if (props.fingerprint.certificate) {
    q.push({
      key: "Certificate",
      query: props.fingerprint.certificate.sha256,
      link: createLink(props.fingerprint.certificate.sha256)
    })
  }

  if (props.fingerprint.tls) {
    const query = `services.jarm.fingerprint:"${props.fingerprint.tls.jarm}"`
    q.push({
      key: "JARM",
      query: query,
      link: createLink(query)
    })
  }

  ;(props.fingerprint.dns.a || []).forEach((record) => {
    const query = `ip:${record.host}`
    q.push({ key: "A", query: query, link: createLink(query) })
  })

  return q
})
</script>

<template>
  <div class="block content is-normal">
    <h4 class="is-size-4">
      <span class="icon">
        <img src="https://www.google.com/s2/favicons?domain=censys.io" alt="shodan" />
      </span>
      Censys
      <span class="icon" @click="toggleIsHidden()">
        <font-awesome-icon icon="caret-down" v-if="isHidden" />
        <font-awesome-icon icon="caret-up" v-else />
      </span>
    </h4>
    <QueryTags :queries="queries" v-if="!isHidden" />
  </div>
</template>
