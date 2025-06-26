import { toNumber } from "./to-number";

test("يجب أن تحول سلسلة نصية رقمية صالحة إلى رقم", () => {
  // Arabic: "Should convert a valid numeric string to a number"
  expect(toNumber("123")).toBe(123);
  expect(toNumber("0")).toBe(0);
  expect(toNumber("-45")).toBe(-45);
  expect(toNumber("3.14")).toBe(3.14);
});

test("يجب أن تحول سلسلة نصية رقمية مع مسافات إلى رقم (سلوك Number())", () => {
  // Arabic: "Should convert a numeric string with spaces to a number (Number() behavior)"
  expect(toNumber(" 123 ")).toBe(123); // Number() trims whitespace
  expect(toNumber("  -45.5  ")).toBe(-45.5);
});

test("يجب أن تعيد NaN لسلسلة نصية غير رقمية", () => {
  // Arabic: "Should return NaN for a non-numeric string"
  expect(toNumber("abc")).toBeNaN();
  expect(toNumber("hello")).toBeNaN();
  expect(toNumber("12a3")).toBeNaN(); // String containing non-numeric chars
});
