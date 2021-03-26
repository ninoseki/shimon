import axios from "axios";

import { Fingerprint } from "@/types";

const client = axios.create({
  headers: {
    Accept: "application/json",
  },
});

export const API = {
  async calculateFingerprint(url: string): Promise<Fingerprint> {
    const res = await client.get<Fingerprint>("/api/fingerprint/calculate", {
      params: { url },
    });
    return res.data;
  },
};
