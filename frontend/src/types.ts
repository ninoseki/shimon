export interface Resource {
  contentType: string;
  md5: string;
  mmh3: number;
  sha256: string;
  url: string;
}

export interface Certificate {
  sha256: string;
  sha1: string;
  serial: string;
}

export interface Fingerprint {
  html: Resource;
  favicon: Resource | null;
  certificate: Certificate | null;
}

export interface ErrorData {
  detail: string;
}
