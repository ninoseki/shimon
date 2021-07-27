<template>
  <div class="box">
    <div class="content is-normal">
      <div class="mt-4 mb-4">
        <h4 class="is-size-4">DNS</h4>
        <table class="table">
          <tr>
            <th>A</th>
            <td>
              <span v-if="fingerprint.dns.a">
                {{ fingerprint.dns.a.map((record) => record.host).join(", ") }}
              </span>
              <span v-else>N/A</span>
            </td>
          </tr>
          <tr>
            <th>AAAA</th>
            <td>
              <span v-if="fingerprint.dns.aaaa">
                {{
                  fingerprint.dns.aaaa.map((record) => record.host).join(", ")
                }}
              </span>
              <span v-else>N/A</span>
            </td>
          </tr>
          <tr>
            <th>CNAME</th>
            <td>
              <span v-if="fingerprint.dns.cname">
                {{
                  fingerprint.dns.cname.map((record) => record.cnmae).join(", ")
                }}
              </span>
              <span v-else>N/A</span>
            </td>
          </tr>
          <tr>
            <th>TXT</th>
            <td>
              <span v-if="fingerprint.dns.txt">
                {{
                  fingerprint.dns.txt.map((record) => record.text).join(", ")
                }}
              </span>
              <span v-else>N/A</span>
            </td>
          </tr>
        </table>
      </div>

      <div class="mt-4 mb-4">
        <h4 class="is-size-4">Whois</h4>
        <table class="table">
          <tr>
            <th>Registrar</th>
            <td>{{ fingerprint.whois.registrar || "N/A" }}</td>
          </tr>
          <tr>
            <th>Registrant organization</th>
            <td>{{ fingerprint.whois.registrantOrganization || "N/A" }}</td>
          </tr>
          <tr>
            <th>Registrant name</th>
            <td>{{ fingerprint.whois.registrantName || "N/A" }}</td>
          </tr>
          <tr>
            <th>Registrant email</th>
            <td>{{ fingerprint.whois.registrantEmail || "N/A" }}</td>
          </tr>
        </table>
      </div>

      <div class="mt-4 mb-4">
        <h4 class="is-size-4">HTML</h4>
        <table class="table">
          <tr>
            <th>URL</th>
            <td>{{ fingerprint.html.url }}</td>
          </tr>
          <tr>
            <th>MMH3</th>
            <td>{{ fingerprint.html.mmh3 }}</td>
          </tr>
          <tr>
            <th>MD5</th>
            <td>{{ fingerprint.html.md5 }}</td>
          </tr>
          <tr>
            <th>SHA1</th>
            <td>{{ fingerprint.html.sha1 }}</td>
          </tr>
          <tr>
            <th>SHA256</th>
            <td>{{ fingerprint.html.sha256 }}</td>
          </tr>
        </table>
      </div>

      <div class="mt-4 mb-4">
        <h4 class="is-size-4">Favicon</h4>
        <table class="table">
          <tr>
            <th>URL</th>
            <td>{{ fingerprint.favicon?.url || "N/A" }}</td>
          </tr>
          <tr>
            <th>MMH3</th>
            <td>{{ fingerprint.favicon?.mmh3 || "N/A" }}</td>
          </tr>
          <tr>
            <th>MD5</th>
            <td>{{ fingerprint.favicon?.md5 || "N/A" }}</td>
          </tr>
          <tr>
            <th>SHA1</th>
            <td>{{ fingerprint.favicon?.sha1 || "N/A" }}</td>
          </tr>
          <tr>
            <th>SHA256</th>
            <td>{{ fingerprint.favicon?.sha256 || "N/A" }}</td>
          </tr>
        </table>
      </div>

      <div class="mt-4 mb-4">
        <h4 class="is-size-4">Tracker</h4>
        <table class="table">
          <tr>
            <th>Google Adsense ID</th>
            <td>{{ fingerprint.tracker.googleAdsenseId || "N/A" }}</td>
          </tr>
          <tr>
            <th>Google Analytics ID</th>
            <td>{{ fingerprint.tracker.googleAnalyticsId || "N/A" }}</td>
          </tr>
        </table>
      </div>

      <div class="mt-4 mb-4">
        <h4 class="is-size-4">Certificate</h4>
        <table class="table">
          <tr>
            <th>SHA1</th>
            <td>{{ fingerprint.certificate?.sha1 || "N/A" }}</td>
          </tr>
          <tr>
            <th>SHA256</th>
            <td>{{ fingerprint.certificate?.sha256 || "N/A" }}</td>
          </tr>
          <tr>
            <th>Serial</th>
            <td>{{ fingerprint.certificate?.serial || "N/A" }}</td>
          </tr>
        </table>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent, PropType } from "vue";

import { Fingerprint } from "@/types";

export default defineComponent({
  name: "Fingerprint",
  props: {
    fingerprint: {
      type: Object as PropType<Fingerprint>,
      required: true,
    },
  },
});
</script>

<style scoped>
table.table {
  table-layout: fixed;
}

table.table th {
  width: 240px;
}

table.table td {
  word-wrap: break-word;
}
</style>
