import angularQuestionItems from '@/content/modules/angular/questions.json'
import javaQuestionItems from '@/content/modules/java/questions.json'
import javascriptQuestionItems from '@/content/modules/javascript/questions.json'
import reactQuestionItems from '@/content/modules/react/questions.json'
import { QuestionItem } from './moduleData.types'
import { QuestionModuleSection } from './QuestionModuleSection'

const interviewQuestions: Record<
  'javascript' | 'react' | 'angular' | 'java',
  QuestionItem[]
> = {
  javascript: javascriptQuestionItems,
  react: reactQuestionItems,
  angular: angularQuestionItems,
  java: javaQuestionItems,
}

export const TechnologyQuestionItem = ({
  technologySlug,
}: {
  technologySlug: 'react' | 'javascript' | 'angular' | 'java'
}) => <QuestionModuleSection items={interviewQuestions[technologySlug]} />
