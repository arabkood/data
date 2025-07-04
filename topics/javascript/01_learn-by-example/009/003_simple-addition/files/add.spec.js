import { add } from "./add.js";

test("يجب أن تجمع رقمين موجبين بشكل صحيح", () => {
  // "Should correctly add two positive numbers"
  expect(add(2, 3)).toBe(5);
  expect(add(10, 20)).toBe(30);
  expect(add(0, 5)).toBe(5); // Test with zero
});

test("يجب أن تجمع رقمًا موجبًا وآخر سالبًا بشكل صحيح", () => {
  //  "Should correctly add a positive and a negative number"
  expect(add(5, -3)).toBe(2);
  expect(add(-10, 7)).toBe(-3);
  expect(add(-5, 5)).toBe(0);
});

test("يجب أن تجمع أرقامًا عشرية بشكل صحيح", () => {
  //  "Should correctly add decimal numbers"
  expect(add(0.1, 0.2)).toBeCloseTo(0.3); // Use toBeCloseTo for floating point comparisons
  expect(add(1.5, 2.5)).toBe(4.0);
  expect(add(-0.5, 0.2)).toBeCloseTo(-0.3);
});
