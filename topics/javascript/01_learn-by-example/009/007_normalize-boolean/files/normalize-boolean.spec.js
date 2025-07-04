import { normalizeBoolean } from "./normalize-boolean";

test('يجب أن تعيد true لكلمة "yes" الصغيرة', () => {
  expect(normalizeBoolean("yes")).toBe(true);
});
test('يجب أن تعيد true لكلمة "YES" الكبيرة', () => {
  expect(normalizeBoolean("YES")).toBe(true);
});
test('يجب أن تعيد true لكلمة "Yes" المختلطة', () => {
  expect(normalizeBoolean("Yes")).toBe(true);
});
test('يجب أن تعيد true لحرف "y" الصغير', () => {
  expect(normalizeBoolean("y")).toBe(true);
});
test('يجب أن تعيد true لحرف "Y" الكبير', () => {
  expect(normalizeBoolean("Y")).toBe(true);
});

test('يجب أن تعيد false لكلمة "no" الصغيرة', () => {
  expect(normalizeBoolean("no")).toBe(false);
});
test('يجب أن تعيد false لكلمة "NO" الكبيرة', () => {
  expect(normalizeBoolean("NO")).toBe(false);
});
test('يجب أن تعيد false لكلمة "No" المختلطة', () => {
  expect(normalizeBoolean("No")).toBe(false);
});
test('يجب أن تعيد false لحرف "n" الصغير', () => {
  expect(normalizeBoolean("n")).toBe(false);
});
test('يجب أن تعيد false لحرف "N" الكبير', () => {
  expect(normalizeBoolean("N")).toBe(false);
});

test("يجب أن تعيد false لنص عشوائي", () => {
  expect(normalizeBoolean("maybe")).toBe(false);
  expect(normalizeBoolean("true")).toBe(false); // The string "true"
  expect(normalizeBoolean("okay")).toBe(false);
});

test("يجب أن تعيد false لنص فارغ", () => {
  expect(normalizeBoolean("")).toBe(false);
});
