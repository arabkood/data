import { maxOfThree } from "./example/max-of-three";

test("يجب أن تعيد الرقم الأول إذا كان هو الأكبر", () => {
  //  "Should return the first number if it is the largest"
  expect(maxOfThree(10, 5, 1)).toBe(10);
  expect(maxOfThree(0, -5, -10)).toBe(0);
});

test("يجب أن تعيد الرقم الثاني إذا كان هو الأكبر", () => {
  //  "Should return the second number if it is the largest"
  expect(maxOfThree(5, 10, 1)).toBe(10);
  expect(maxOfThree(-5, 0, -10)).toBe(0);
});

test("يجب أن تعيد الرقم الثالث إذا كان هو الأكبر", () => {
  // "Should return the third number if it is the largest"
  expect(maxOfThree(1, 5, 10)).toBe(10);
  expect(maxOfThree(-10, -5, 0)).toBe(0);
});
