import { convertToColonSeparatedText } from "@/utils";

describe("convertToColonSeparatedText", () => {
  it.each([
    ["1111", "11:11"],
    [
      "0a28a6eb176ea9cc596f4c73fd897efbd32dca2a",
      "0a:28:a6:eb:17:6e:a9:cc:59:6f:4c:73:fd:89:7e:fb:d3:2d:ca:2a",
    ],
  ])("should convert to colon separated value", (string, expected) => {
    expect(convertToColonSeparatedText(string)).toBe(expected);
  });
});
