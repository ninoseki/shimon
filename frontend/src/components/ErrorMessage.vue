<template>
  <article class="message is-warning">
    <div class="message-header">
      <p>Warning</p>
    </div>
    <div class="message-body">
      <div v-if="error?.detail">
        <VueJsonPretty :data="anyError"></VueJsonPretty>
      </div>
      <div v-else>Something went wrong...</div>
    </div>
  </article>
</template>

<script lang="ts">
import "vue-json-pretty/lib/styles.css"

import { computed, defineComponent, type PropType } from "vue"
import VueJsonPretty from "vue-json-pretty"

import type { ErrorData } from "@/types"

export default defineComponent({
  name: "ErrorMessage",
  props: {
    error: {
      type: Object as PropType<ErrorData>,
      required: false
    }
  },
  components: { VueJsonPretty },
  setup(props) {
    const anyError = computed(() => {
      return props.error as any
    })
    return { anyError }
  }
})
</script>
