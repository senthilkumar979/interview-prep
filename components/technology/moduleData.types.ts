export interface ExampleCode {
  title: string;
  language: string;
  code: string;
  explanation: string;
}

export interface QuestionLink {
  label: string;
  href: string;
}

export interface QuestionItem {
  id: string;
  question: string;
  difficulty: string;
  category: string;
  tags: string[];
  preview: string;
  answer: string;
  examples: ExampleCode[];
  tip: string;
  links?: QuestionLink[];
}

export interface KataItem {
  id: string;
  title: string;
  difficulty: string;
  category: string;
  description: string;
  starterCode: string;
  solution: string;
}

export interface DebugAnswer {
  line: number;
  title: string;
  explanation: string;
  fix: string;
}

export interface DebugItem {
  id: string;
  title: string;
  difficulty: string;
  category: string;
  file: string;
  answers: DebugAnswer[];
}

export interface FillAnswer {
  line: number;
  placeholder: string;
  value: string;
  explanation: string;
}

export interface FillItem {
  id: string;
  title: string;
  difficulty: string;
  category: string;
  file: string;
  answers: FillAnswer[];
}

export interface McqOption {
  id: string;
  text: string;
}

export interface McqItem {
  id: string;
  question: string;
  difficulty: string;
  category: string;
  options: McqOption[];
  correctOptionId: string;
  explanation: string;
}

export interface RapidFireItem {
  id: string;
  prompt: string;
  expectedAnswer: string;
  category: string;
  difficulty: string;
}

export interface OutputPredictionItem {
  id: string;
  title: string;
  difficulty: string;
  category: string;
  file: string;
  expectedOutput: string;
  explanation: string;
}

export interface SystemDesignItem {
  id: string;
  title: string;
  difficulty: string;
  category: string;
  problem: string;
  requirements: string[];
  approach: string;
}
