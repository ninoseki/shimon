import axios from "axios"

import { CountSchema, type CountType, type Fingerprint } from "@/types"

const client = axios.create({
  headers: {
    Accept: "application/json"
  }
})

export const API = {
  async calculateFingerprint(url: string): Promise<Fingerprint> {
    const res = await client.get<Fingerprint>("/api/fingerprint/calculate", {
      params: { url }
    })
    return res.data
  },
  async count(service: string, query: string): Promise<CountType> {
    const res = await client.get(`/api/counters/${service}`, {
      params: { query }
    })
    return CountSchema.parse(res.data)
  }
}
