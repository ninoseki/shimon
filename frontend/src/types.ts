import { z } from "zod"

export const ValidationErrorSchema = z.object({
  loc: z.array(z.string()),
  msg: z.string(),
  type: z.string()
})

export const ErrorDataSchema = z.object({
  detail: z.union([z.string(), z.array(ValidationErrorSchema)])
})

export type ErrorDataType = z.infer<typeof ErrorDataSchema>

export const CountSchema = z.object({
  count: z.number()
})

export type CountType = z.infer<typeof CountSchema>

// TODO: replace them with Zod
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

export interface Query {
  key: string
  query: string
  link: string
}
