export interface Hashes {
  contentType: string;
  md5: string;
  mmh3: number;
  sha256: string;
  url: string;
}

export type QueryType = "html" | "favicon";

export interface ValidationError {
  loc: string[];
  msg: string;
  type: string;
}

export interface ErrorData {
  detail: string | ValidationError[];
}
