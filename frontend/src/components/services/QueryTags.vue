<script setup lang="ts">
import { type PropType } from "vue"

import QueryTag from "@/components/services/QueryTag.vue"
import type { Query } from "@/types"

defineProps({
  queries: {
    type: Array as PropType<Query[]>,
    required: true
  },
  service: {
    type: String,
    required: false
  }
})
</script>

<template>
  <div class="field is-grouped is-grouped-multiline">
    <QueryTag :query="query" :service="service" v-for="(query, index) in queries" :key="index" />
  </div>
</template>
