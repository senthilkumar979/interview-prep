export const technologyModules = [
  "Interview Questions",
  "Coding Exercises",
  "Debugging",
  "Fill in blanks",
  "MCQ",
  "Rapid Fire",
  "Output prediction",
  "System design",
] as const;

export type TechnologyModule = (typeof technologyModules)[number];
