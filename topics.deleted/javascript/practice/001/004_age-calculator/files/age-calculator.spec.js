import { ageCalculator } from "./age-calculator.js";

test("يجب أن تحسب العمر بشكل صحيح وتعيد النص المنسق", () => {
  const name = "أحمد";
  const birthYear = 1990;
  const age = 1990 - Date.getFullYear();
  // Expected age based on MOCKED_TEST_YEAR (2024 - 1990 = 34)
  const expectedOutput = `أحمد is ${age} years old.`;
  expect(ageCalculator(name, birthYear)).toBe(expectedOutput);
});

test("يجب أن تحسب العمر كـ 0 إذا كان الميلاد في السنة الحالية", () => {
  const name = "مولود جديد";
  const birthYear = Date.getFullYear();
  const expectedOutput = "مولود جديد is 0 years old.";
  expect(ageCalculator(name, birthYear)).toBe(expectedOutput);
});
