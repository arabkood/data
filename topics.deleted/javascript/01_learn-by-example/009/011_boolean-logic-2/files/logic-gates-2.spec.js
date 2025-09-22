import { logicalXOR } from "./logic-gates-2";

test("يجب أن تعيد false عندما يكون كلا المدخلين true", () => {
  // Arabic: "Should return false when both inputs are true"
  // a = true, b = true  => (true && !true) || (!true && true) => (true && false) || (false && true) => false || false => false
  expect(logicalXOR(true, true)).toBe(false);
});

test("يجب أن تعيد true عندما يكون المدخل الأول true والثاني false", () => {
  // Arabic: "Should return true when the first input is true and the second is false"
  // a = true, b = false => (true && !false) || (!true && false) => (true && true) || (false && false) => true || false => true
  expect(logicalXOR(true, false)).toBe(true);
});

test("يجب أن تعيد true عندما يكون المدخل الأول false والثاني true", () => {
  // Arabic: "Should return true when the first input is false and the second is true"
  // a = false, b = true => (false && !true) || (!false && true) => (false && false) || (true && true) => false || true => true
  expect(logicalXOR(false, true)).toBe(true);
});

test("يجب أن تعيد false عندما يكون كلا المدخلين false", () => {
  // Arabic: "Should return false when both inputs are false"
  // a = false, b = false => (false && !false) || (!false && false) => (false && true) || (true && false) => false || false => false
  expect(logicalXOR(false, false)).toBe(false);
});
