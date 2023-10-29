<template>
  <div class="tags has-addons are-medium" v-for="(query, index) in queries" :key="index">
    <span class="tag is-dark">{{ query.key }}</span>
    <a class="tag is-info" target="_blank" :href="query.link">{{ query.query }}</a>
  </div>
</template>

<script lang="ts">
import { defineComponent, type PropType } from "vue"

import type { Query } from "@/types"

export default defineComponent({
  name: "QueryTagsComponent",
  props: {
    queries: {
      type: Array as PropType<Query[]>,
      required: true
    }
  }
})
</script>
