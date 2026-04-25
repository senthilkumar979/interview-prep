export interface InterviewQuestion {
  id: string;
  title: string;
  description: string;
  difficulty: string;
  category: string;
  technology: string;
  snippet: string;
}

export interface LandingContent {
  brand: {
    name: string;
    tagline: string;
  };
  technologies: string[];
  questions: InterviewQuestion[];
}
