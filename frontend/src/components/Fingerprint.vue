<template>
  <div class="box">
    <VueJsonPretty :data="anyFingerprint"></VueJsonPretty>
  </div>
</template>

<script lang="ts">
import "vue-json-pretty/lib/styles.css"

import { computed, defineComponent, type PropType } from "vue"
import VueJsonPretty from "vue-json-pretty"

import type { Fingerprint } from "@/types"

export default defineComponent({
  name: "FingerprintComponent",
  props: {
    fingerprint: {
      type: Object as PropType<Fingerprint>,
      required: true
    }
  },
  components: {
    VueJsonPretty
  },
  setup(props) {
    const anyFingerprint = computed(() => {
      return props.fingerprint as any
    })
    return { anyFingerprint }
  }
})
</script>
