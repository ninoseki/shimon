<script setup lang="ts">
import { ref } from "vue"
import { useAsyncTask } from "vue-concurrency"

import { API } from "@/api"
import ErrorMessage from "@/components/ErrorMessage.vue"
import FingerprintComponent from "@/components/Fingerprint.vue"
import Loading from "@/components/LoadingItem.vue"
import BinaryEdge from "@/components/services/BinaryEdgeItem.vue"
import Censys from "@/components/services/CensysItem.vue"
import Fofa from "@/components/services/FofaItem.vue"
import Onyphe from "@/components/services/OnypheItem.vue"
import SecurityTrails from "@/components/services/SecurityTrailsItem.vue"
import Shodan from "@/components/services/ShodanItem.vue"
import SpyOnWeb from "@/components/services/SpyOnWebItem.vue"
import Urlscan from "@/components/services/UrlscanItem.vue"
import VirusTotal from "@/components/services/VirusTotalItem.vue"
import ZoomEye from "@/components/services/ZoomEyeItem.vue"
import type { Fingerprint } from "@/types"

const url = ref<string>("https://example.com")

const calculateTask = useAsyncTask<Fingerprint, []>(async () => {
  return await API.calculateFingerprint(url.value || "")
})

const calculate = async () => {
  if (!url.value) {
    return
  }

  await calculateTask.perform()
}
</script>

<template>
  <div class="field">
    <div class="control is-clearfix">
      <input
        type="url"
        autocomplete="on"
        class="input"
        placeholder="http://example.com"
        v-model="url"
      />
    </div>
  </div>
  <div class="block has-text-centered">
    <button type="button" class="button is-light" @click="calculate">
      <span>Calculate</span>
    </button>
  </div>
  <Loading v-if="calculateTask.isRunning" />
  <ErrorMessage :error="calculateTask.last?.error" v-if="calculateTask.isError" />
  <div v-if="calculateTask.last?.value">
    <FingerprintComponent :fingerprint="calculateTask.last.value" />
    <hr />
    <Shodan :fingerprint="calculateTask.last.value" />
    <Censys :fingerprint="calculateTask.last.value" />
    <BinaryEdge :fingerprint="calculateTask.last.value" />
    <Fofa :fingerprint="calculateTask.last.value" />
    <Onyphe :fingerprint="calculateTask.last.value" />
    <SecurityTrails :fingerprint="calculateTask.last.value" />
    <SpyOnWeb :fingerprint="calculateTask.last.value" />
    <Urlscan :fingerprint="calculateTask.last.value" />
    <VirusTotal :fingerprint="calculateTask.last.value" />
    <ZoomEye :fingerprint="calculateTask.last.value" />
  </div>
</template>
