<script setup lang="ts">
import { onMounted, type PropType } from "vue"
import { useAsyncTask } from "vue-concurrency"

import { API } from "@/api"
import type { CountType, Query } from "@/types"

const props = defineProps({
  query: {
    type: Object as PropType<Query>,
    required: true
  },
  service: {
    type: String,
    required: false
  }
})

const countTask = useAsyncTask<CountType, []>(async () => {
  if (!props.service) {
    throw Error("service is not set or not supported yet")
  }
  return await API.count(props.service, props.query.query)
})

onMounted(async () => {
  await countTask.perform()
})
</script>

<template>
  <div class="control">
    <div class="tags are-medium has-addons">
      <span class="tag is-dark">{{ query.key }}</span>
      <a class="tag is-info" target="_blank" :href="query.link">{{ query.query }}</a>
      <span class="tag" v-if="countTask.performCount > 0">{{
        countTask.last?.value?.count?.toString() || "-"
      }}</span>
    </div>
  </div>
</template>
