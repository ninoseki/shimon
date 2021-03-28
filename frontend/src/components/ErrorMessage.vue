<template>
  <article class="message is-warning">
    <div class="message-header">
      <p>Warning</p>
    </div>
    <div class="message-body">
      {{ error?.detail || "Something went wrong..." }}
    </div>
  </article>
</template>

<script lang="ts">
import { defineComponent, PropType } from "vue";

import { ErrorData } from "@/types";

export default defineComponent({
  name: "ErrorMessage",
  props: {
    error: {
      type: Object as PropType<ErrorData>,
      required: false,
    },
  },
});
</script>
