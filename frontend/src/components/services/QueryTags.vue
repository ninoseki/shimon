<template>
  <div class="field is-grouped is-grouped-multiline">
    <div class="control" v-for="(query, index) in queries" :key="index">
      <div class="tags are-medium has-addons">
        <span class="tag is-dark">{{ query.key }}</span>
        <a class="tag is-info" target="_blank" :href="query.link">{{ query.query }}</a>
      </div>
    </div>
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
