import javascriptQuestionItems from '@/content/modules/javascript/questions.json'
import reactQuestionItems from '@/content/modules/react/questions.json'
import { QuestionItem } from './moduleData.types'
import { QuestionModuleSection } from './QuestionModuleSection'

const interviewQuestions: Record<
  'javascript' | 'react' | 'java',
  QuestionItem[]
> = {
  javascript: javascriptQuestionItems,
  react: reactQuestionItems,
  java: [],
}

export const TechnologyQuestionItem = ({
  technologySlug,
}: {
  technologySlug: 'react' | 'javascript'
}) => <QuestionModuleSection items={interviewQuestions[technologySlug]} />
