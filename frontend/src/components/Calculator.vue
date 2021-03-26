<template>
  <div>
    <div class="field">
      <div class="control is-clearfix">
        <input type="url" autocomplete="on" class="input" v-model="url" />
      </div>
    </div>
    <div class="has-text-centered">
      <button type="button" class="button is-light" @click="calculate">
        <span>Calculate</span>
      </button>
    </div>

    <hr />

    <div v-if="calculateTask.isRunning">
      <div class="has-text-centered">
        <div class="fa-3x">
          <i class="fas fa-spinner fa-spin"></i>
        </div>
      </div>
    </div>

    <div
      class="notification is-warning"
      v-else-if="calculateTask.isError && calculateTask.last"
    >
      <p>{{ calculateTask.last.error.response.data.detail }}</p>
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
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref } from "vue";
import { useAsyncTask } from "vue-concurrency";

import { API } from "@/api";
import FingerprintComponent from "@/components/Fingerprint.vue";
import BinaryEdge from "@/components/services/BinaryEdge.vue";
import Censys from "@/components/services/Censys.vue";
import Onyphe from "@/components/services/Onyphe.vue";
import Shodan from "@/components/services/Shodan.vue";
import Spyse from "@/components/services/Spyse.vue";
import Urlscan from "@/components/services/Urlscan.vue";
import { Fingerprint } from "@/types";

export default defineComponent({
  name: "Calculator",
  components: {
    BinaryEdge,
    Censys,
    FingerprintComponent,
    Onyphe,
    Shodan,
    Spyse,
    Urlscan,
  },
  setup() {
    const url = ref<string | undefined>(undefined);

    const calculateTask = useAsyncTask<Fingerprint, []>(async () => {
      return await API.calculateFingerprint(url.value || "");
    });

    const calculate = async () => {
      if (url.value === undefined) {
        return;
      }

      await calculateTask.perform();
    };

    return { url, calculate, calculateTask };
  },
});
</script>

<style scoped>
.links {
  margin-top: 20px;
  margin-bottom: 20px;
}
</style>
