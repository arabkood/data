import { logicalAND, logicalOR, logicalNOT } from "./logic-gates-1";

describe("دالة logicalAND (و المنطقية)", () => {
  // Arabic: "logicalAND Function (Logical AND)"
  test("يجب أن تعيد true عندما يكون كلا المدخلين true", () => {
    // Arabic: "Should return true when both inputs are true"
    expect(logicalAND(true, true)).toBe(true);
  });

  test("يجب أن تعيد false عندما يكون المدخل الأول true والثاني false", () => {
    // Arabic: "Should return false when first input is true and second is false"
    expect(logicalAND(true, false)).toBe(false);
  });

  test("يجب أن تعيد false عندما يكون المدخل الأول false والثاني true", () => {
    // Arabic: "Should return false when first input is false and second is true"
    expect(logicalAND(false, true)).toBe(false);
  });

  test("يجب أن تعيد false عندما يكون كلا المدخلين false", () => {
    // Arabic: "Should return false when both inputs are false"
    expect(logicalAND(false, false)).toBe(false);
  });
});

describe("دالة logicalOR (أو المنطقية)", () => {
  // Arabic: "logicalOR Function (Logical OR)"
  test("يجب أن تعيد true عندما يكون كلا المدخلين true", () => {
    // Arabic: "Should return true when both inputs are true"
    expect(logicalOR(true, true)).toBe(true);
  });

  test("يجب أن تعيد true عندما يكون المدخل الأول true والثاني false", () => {
    // Arabic: "Should return true when first input is true and second is false"
    expect(logicalOR(true, false)).toBe(true);
  });

  test("يجب أن تعيد true عندما يكون المدخل الأول false والثاني true", () => {
    // Arabic: "Should return true when first input is false and second is true"
    expect(logicalOR(false, true)).toBe(true);
  });

  test("يجب أن تعيد false عندما يكون كلا المدخلين false", () => {
    // Arabic: "Should return false when both inputs are false"
    expect(logicalOR(false, false)).toBe(false);
  });
});

describe("دالة logicalNOT (ليس المنطقية)", () => {
  // Arabic: "logicalNOT Function (Logical NOT)"
  test("يجب أن تعيد false عندما يكون المدخل true", () => {
    // Arabic: "Should return false when the input is true"
    expect(logicalNOT(true)).toBe(false);
  });

  test("يجب أن تعيد true عندما يكون المدخل false", () => {
    // Arabic: "Should return true when the input is false"
    expect(logicalNOT(false)).toBe(true);
  });
});
