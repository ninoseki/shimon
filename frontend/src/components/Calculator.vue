<template>
  <div>
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
    <div class="has-text-centered">
      <button type="button" class="button is-light" @click="calculate">
        <span>Calculate</span>
      </button>
    </div>
    <hr />
    <div v-if="calculateTask.isRunning">
      <Loading></Loading>
    </div>
    <div v-else-if="calculateTask.isError && calculateTask.last">
      <ErrorMessage :error="getErrorData()"></ErrorMessage>
    </div>
    <div v-else>
      <div v-if="calculateTask.last?.value">
        <FingerprintComponent :fingerprint="calculateTask.last.value"></FingerprintComponent>
        <hr />
        <BinaryEdge :fingerprint="calculateTask.last.value"></BinaryEdge>
        <Censys :fingerprint="calculateTask.last.value"></Censys>
        <Fofa :fingerprint="calculateTask.last.value"></Fofa>
        <Onyphe :fingerprint="calculateTask.last.value"></Onyphe>
        <SecurityTrails :fingerprint="calculateTask.last.value"></SecurityTrails>
        <Shodan :fingerprint="calculateTask.last.value"></Shodan>
        <SpyOnWeb :fingerprint="calculateTask.last.value"></SpyOnWeb>
        <Urlscan :fingerprint="calculateTask.last.value"></Urlscan>
        <VirusTotal :fingerprint="calculateTask.last.value"></VirusTotal>
        <ZoomEye :fingerprint="calculateTask.last.value"></ZoomEye>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref } from "vue"
import { useAsyncTask } from "vue-concurrency"

import { API } from "@/api"
import ErrorMessage from "@/components/ErrorMessage.vue"
import FingerprintComponent from "@/components/Fingerprint.vue"
import Loading from "@/components/Loading.vue"
import BinaryEdge from "@/components/services/BinaryEdge.vue"
import Censys from "@/components/services/Censys.vue"
import Fofa from "@/components/services/Fofa.vue"
import Onyphe from "@/components/services/Onyphe.vue"
import SecurityTrails from "@/components/services/SecurityTrails.vue"
import Shodan from "@/components/services/Shodan.vue"
import SpyOnWeb from "@/components/services/SpyOnWeb.vue"
import Urlscan from "@/components/services/Urlscan.vue"
import VirusTotal from "@/components/services/VirusTotal.vue"
import ZoomEye from "@/components/services/ZoomEye.vue"
import type { ErrorData, Fingerprint } from "@/types"

export default defineComponent({
  name: "CalculatorComponent",
  components: {
    BinaryEdge,
    Censys,
    ErrorMessage,
    FingerprintComponent,
    Fofa,
    Loading,
    Onyphe,
    SecurityTrails,
    Shodan,
    SpyOnWeb,
    Urlscan,
    VirusTotal,
    ZoomEye
  },
  setup() {
    const url = ref<string>("https://example.com")

    const calculateTask = useAsyncTask<Fingerprint, []>(async () => {
      return await API.calculateFingerprint(url.value || "")
    })

    const calculate = async () => {
      if (url.value === undefined) {
        return
      }

      await calculateTask.perform()
    }

    const getErrorData = (): ErrorData | undefined => {
      if (calculateTask.isError && calculateTask.last) {
        const data = calculateTask.last.error.response.data as ErrorData
        return data
      }

      return undefined
    }

    return { url, calculate, calculateTask, getErrorData }
  }
})
</script>
