export interface Resource {
  contentType: string
  md5: string
  mmh3: number
  sha1: string
  sha256: string
  url: string
}

export interface Favicon extends Resource {}

export interface Certificate {
  sha256: string
  sha1: string
  serial: string
}

export interface A {
  host: string
  ttl: number
}

export interface CNAME {
  cnmae: string
  ttl: number
}

export interface TXT {
  text: string
  ttl: number
}
export interface DNS {
  a?: A[]
  aaaa?: A[]
  cname?: CNAME[]
  txt?: TXT[]
}

export interface Tracker {
  googleAdsenseId?: string
  googleAnalyticsId?: string
}

export interface Whois {
  registrantEmail?: string
  registrantName?: string
  registrantOrganization?: string
  registrar?: string
}

export interface HTML extends Resource {
  title?: string
}

export interface TLS {
  jarm: string
}

export interface Headers {
  [key: string]: string
}

export interface Fingerprint {
  html: HTML
  dns: DNS
  tracker: Tracker
  whois: Whois
  favicon?: Favicon
  certificate?: Certificate
  tls?: TLS
  headers: Headers
}

export interface ErrorData {
  detail: string
}

export interface Query {
  key: string
  query: string
  link: string
}
