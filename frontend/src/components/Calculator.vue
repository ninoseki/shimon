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
        <FingerprintComponent
          :fingerprint="calculateTask.last.value"
        ></FingerprintComponent>

        <div class="columns is-multiline is-mobile">
          <BinaryEdge :fingerprint="calculateTask.last.value"></BinaryEdge>
          <Censys :fingerprint="calculateTask.last.value"></Censys>
          <Onyphe :fingerprint="calculateTask.last.value"></Onyphe>
          <Shodan :fingerprint="calculateTask.last.value"></Shodan>
          <Spyse :fingerprint="calculateTask.last.value"></Spyse>
          <Urlscan :fingerprint="calculateTask.last.value"></Urlscan>
          <VirusTotal :fingerprint="calculateTask.last.value"></VirusTotal>
          <SecurityTrails
            :fingerprint="calculateTask.last.value"
          ></SecurityTrails>
          <SpyOnWeb :fingerprint="calculateTask.last.value"></SpyOnWeb>
          <DomainBigData
            :fingerprint="calculateTask.last.value"
          ></DomainBigData>
          <DomainWatch :fingerprint="calculateTask.last.value"></DomainWatch>
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref } from "vue";
import { useAsyncTask } from "vue-concurrency";

import { API } from "@/api";
import ErrorMessage from "@/components/ErrorMessage.vue";
import FingerprintComponent from "@/components/Fingerprint.vue";
import Loading from "@/components/Loading.vue";
import BinaryEdge from "@/components/services/BinaryEdge.vue";
import Censys from "@/components/services/Censys.vue";
import DomainBigData from "@/components/services/DomainBigData.vue";
import DomainWatch from "@/components/services/DomainWatch.vue";
import Onyphe from "@/components/services/Onyphe.vue";
import SecurityTrails from "@/components/services/SecurityTrails.vue";
import Shodan from "@/components/services/Shodan.vue";
import SpyOnWeb from "@/components/services/SpyOnWeb.vue";
import Spyse from "@/components/services/Spyse.vue";
import Urlscan from "@/components/services/Urlscan.vue";
import VirusTotal from "@/components/services/VirusTotal.vue";
import { ErrorData, Fingerprint } from "@/types";

export default defineComponent({
  name: "Calculator",
  components: {
    BinaryEdge,
    Censys,
    ErrorMessage,
    FingerprintComponent,
    Loading,
    Onyphe,
    Shodan,
    Spyse,
    Urlscan,
    VirusTotal,
    SecurityTrails,
    SpyOnWeb,
    DomainWatch,
    DomainBigData,
  },
  setup() {
    const url = ref<string>("https://example.com");

    const calculateTask = useAsyncTask<Fingerprint, []>(async () => {
      return await API.calculateFingerprint(url.value || "");
    });

    const calculate = async () => {
      if (url.value === undefined) {
        return;
      }

      await calculateTask.perform();
    };

    const getErrorData = (): ErrorData | undefined => {
      if (calculateTask.isError && calculateTask.last) {
        const data = calculateTask.last.error.response.data as ErrorData;
        return data;
      }

      return undefined;
    };

    return { url, calculate, calculateTask, getErrorData };
  },
});
</script>
