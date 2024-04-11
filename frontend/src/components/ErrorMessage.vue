<script setup lang="ts">
import "vue-json-pretty/lib/styles.css"

import { AxiosError } from "axios"
import { computed } from "vue"
import VueJsonPretty from "vue-json-pretty"

import type { ErrorDataType } from "@/types"

const props = defineProps({
  error: {
    type: AxiosError,
    required: true
  }
})

const data = computed<ErrorDataType | undefined>(() => {
  if (props.error.response) {
    return props.error.response?.data as ErrorDataType
  }
  return undefined
})
</script>

<template>
  <div class="notification is-danger is-light">
    <div v-if="data?.detail">
      <div v-if="typeof data.detail === 'string'">
        {{ data.detail }}
      </div>
      <VueJsonPretty :data="data.detail" v-else />
    </div>
    <p v-else>{{ error }}</p>
  </div>
</template>
