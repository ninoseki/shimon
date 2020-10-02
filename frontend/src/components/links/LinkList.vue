<template>
  <div class="box">
    <BinaryEdge v-bind:hashes="hashes" />
    <hr />
    <Onyphe v-bind:hashes="hashes" />
    <hr />
    <Shodan v-bind:hashes="hashes" />
    <hr />
    <Spyse v-bind:hashes="hashes" />
  </div>
</template>

<script lang="ts">
import { Component, Prop, Vue } from "vue-property-decorator";

import { Hashes } from "@/types";

import BinaryEdge from "./BinaryEdge.vue";
import Onyphe from "./Onyphe.vue";
import Shodan from "./Shodan.vue";
import Spyse from "./Spyse.vue";

@Component({
  components: {
    BinaryEdge,
    Onyphe,
    Shodan,
    Spyse,
  },
})
export default class LinkList extends Vue {
  @Prop() hashes!: Hashes;
}
</script>
