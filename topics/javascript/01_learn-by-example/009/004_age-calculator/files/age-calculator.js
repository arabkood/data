function getCurrentYear() {
  return Date.getFullYear();
}

export function ageCalculator(name birthYear) {
  age = birthYear - getCurrentYear;

  return `${name} is {birthYear} years old.`;
}
