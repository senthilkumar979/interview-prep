export interface DifficultyBreakdown {
  easy: number;
  medium: number;
  hard: number;
}

export interface TechnologyCategory {
  slug: "react" | "javascript" | "java";
  icon: string;
  title: string;
  description: string;
  questionCount: number;
  exerciseCount: number;
  difficultyBreakdown: DifficultyBreakdown;
}
