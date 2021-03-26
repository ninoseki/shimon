export function convertToColonSeparatedText(text: string): string {
  const span = 2;
  const splitter = ":";

  let ret = text.slice(0, span);
  let remaining = text.slice(span);

  while (remaining) {
    const v = remaining.slice(0, span);
    remaining = remaining.slice(v.length);
    ret += splitter + v;
  }

  return ret;
}
