export interface Resource {
  contentType: string;
  md5: string;
  mmh3: number;
  sha1: string;
  sha256: string;
  url: string;
}

export interface Certificate {
  sha256: string;
  sha1: string;
  serial: string;
}

export interface A {
  host: string;
  ttl: number;
}

export interface CNAME {
  cnmae: string;
  ttl: number;
}

export interface TXT {
  text: string;
  ttl: number;
}
export interface DNS {
  a: A[] | null;
  aaaa: A[] | null;
  cname: CNAME[] | null;
  txt: TXT[] | null;
}

export interface Tracker {
  googleAdsenseId: string | null;
  googleAnalyticsId: string | null;
}

export interface Whois {
  registrantEmail: string | null;
  registrantName: string | null;
  registrantOrganization: string | null;
  registrar: string | null;
}

export interface Fingerprint {
  html: Resource;
  dns: DNS;
  tracker: Tracker;
  whois: Whois;
  favicon: Resource | null;
  certificate: Certificate | null;
}

export interface ErrorData {
  detail: string;
}
