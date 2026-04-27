'use client'

import { MarkdownContent } from '@/components/shared/MarkdownContent'
import { QuestionItem } from '@/components/technology/moduleData.types'
import { Badge } from '@/components/ui/badge'
import { Button } from '@/components/ui/button'
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card'
import {
  BadgeQuestionMark,
  Brain,
  Check,
  ChevronDown,
  ChevronUp,
  CodeIcon,
  Copy,
  Lightbulb,
  LinkIcon,
  SignpostIcon,
  SquareArrowOutUpRightIcon,
} from 'lucide-react'
import Link from 'next/link'
import { useState } from 'react'

interface QuestionCardProps {
  item: QuestionItem
  number: number
}

function getDifficultyBadgeClass(difficulty: string): string {
  const normalizedDifficulty = difficulty.toLowerCase()
  if (normalizedDifficulty === 'beginner') return 'difficulty-advanced'
  if (normalizedDifficulty === 'intermediate') return 'difficulty-intermediate'
  if (normalizedDifficulty === 'expert') return 'difficulty-expert'
  if (normalizedDifficulty === 'advanced') return 'difficulty-advanced'
  return 'border-border bg-muted text-muted-foreground rounded-lg'
}

function getCategoryBadgeClass(category: string): string {
  const normalizedCategory = category.toLowerCase()
  if (!normalizedCategory) return 'border-border bg-muted text-muted-foreground'
  const categoryBadgeVariants = [
    'border-primary/30 bg-primary/10 text-primary',
    'border-indigo-500/30 bg-indigo-500/10 text-indigo-700',
    'border-emerald-500/30 bg-emerald-500/10 text-emerald-700',
    'border-amber-500/30 bg-amber-500/10 text-amber-700',
    'border-fuchsia-500/30 bg-fuchsia-500/10 text-fuchsia-700',
  ] as const
  const hash = normalizedCategory
    .split('')
    .reduce((accumulator, char) => accumulator + char.charCodeAt(0), 0)
  return categoryBadgeVariants[hash % categoryBadgeVariants.length]
}

export const QuestionCard = ({ item, number }: QuestionCardProps) => {
  const [isExpanded, setIsExpanded] = useState(false)
  const [copiedExampleTitle, setCopiedExampleTitle] = useState<string | null>(null)

  const onCopyExampleCode = async (code: string, title: string) => {
    await navigator.clipboard.writeText(code)
    setCopiedExampleTitle(title)
    window.setTimeout(() => {
      setCopiedExampleTitle((currentTitle) =>
        currentTitle === title ? null : currentTitle,
      )
    }, 1600)
  }

  return (
    <div className="space-y-3">
      <Card className={isExpanded ? 'border-2' : 'border-none'}>
        <CardHeader
          className="space-y-1 cursor-pointer"
          onClick={() => setIsExpanded((current) => !current)}
        >
          <CardTitle className="text-lg flex items-center justify-between">
            <div className="flex items-center text-deep-space-blue gap-2">
              <BadgeQuestionMark className="h-4 w-4" />#{number}.{' '}
              {item.question}
            </div>
            <Button type="button" variant="outline">
              {isExpanded ? (
                <ChevronDown className="h-4 w-4" />
              ) : (
                <ChevronUp className="h-4 w-4" />
              )}
            </Button>
          </CardTitle>
          <div className="flex flex-wrap gap-2">
            <Badge
              className={`px-2 capitalize tracking-wide py-1 text-xs font-medium rounded-lg ${getDifficultyBadgeClass(
                item.difficulty,
              )}`}
            >
              {item.difficulty}
            </Badge>
            <Badge
              className={`px-2 capitalize tracking-wide py-1 text-xs font-medium rounded-lg ${getCategoryBadgeClass(
                item.category,
              )}`}
            >
              {item.category}
            </Badge>
          </div>
        </CardHeader>
        {isExpanded ? (
          <CardContent className="space-y-4 text-sm">
            <Card className="border-none bg-muted">
              <CardHeader>
                <CardTitle className="text-base font-semibold uppercase tracking-wide ">
                  <Brain className="h-4 w-4" />
                  Explanation
                </CardTitle>
              </CardHeader>
              <CardContent>
                <MarkdownContent content={item.answer} />
              </CardContent>
            </Card>

            <div className="flex flex-col items-center justify-between gap-4 lg:flex-row lg:items-start">
              {item.examples.map((example, index) => (
                <Card key={example.title} className="w-full min-w-0">
                  <CardHeader className="space-y-2">
                    <div className="flex items-center justify-between gap-2">
                      <CardTitle className="text-base uppercase tracking-wide">
                        <CodeIcon className="h-4 w-4" />
                        Code example #{index + 1}
                      </CardTitle>
                      <Button
                        aria-label={`Copy code for ${example.title}`}
                        className="shrink-0 border-none rounded-lg"
                        onClick={() => onCopyExampleCode(example.code, example.title)}
                        size="sm"
                        type="button"
                        variant="outline"
                      >
                        {copiedExampleTitle === example.title ? (
                          <>
                            <Check className="h-4 w-4" />
                            Copied
                          </>
                        ) : (
                          <>
                            <Copy className="h-4 w-4" />
                            Copy
                          </>
                        )}
                      </Button>
                    </div>
                    <p className="text-xs text-muted-foreground">
                      {example.title}
                    </p>
                  </CardHeader>
                  <CardContent className="min-w-0 space-y-3">
                    <div className="w-full min-w-0 overflow-x-auto">
                      <MarkdownContent
                        className="min-w-0"
                        content={`\`\`\`${example.language}\n${example.code}\n\`\`\``}
                      />
                    </div>
                    <div className="p-3 text-sm text-muted-foreground">
                      {example.explanation}
                    </div>
                  </CardContent>
                </Card>
              ))}
            </div>
            <div className="grid grid-cols-1 gap-2 lg:grid-cols-2">
              <Card className="border-none bg-muted">
                <CardHeader>
                  <CardTitle className="text-base uppercase tracking-wide">
                    <Lightbulb className="h-4 w-4" />
                    Tip
                  </CardTitle>
                </CardHeader>
                <CardContent>
                  <p className="text-sm flex items-start gap-2 pl-5">
                    <SignpostIcon className="h-5 w-5" />
                    <span>{item.tip}</span>
                  </p>
                </CardContent>
              </Card>

              {item.links?.length ? (
                <Card className="border-none bg-muted">
                  <CardHeader>
                    <CardTitle className="text-base uppercase tracking-wide">
                      <LinkIcon className="h-4 w-4" />
                      Links
                    </CardTitle>
                  </CardHeader>
                  <CardContent>
                    <ul className="list-disc space-y-1 pl-5">
                      {item.links.map((link) => (
                        <li
                          key={link.href}
                          className="cursor-pointer list-none flex items-center gap-2"
                        >
                          <SquareArrowOutUpRightIcon className="h-3 w-3" />
                          <Link
                            className="underline-offset-2 hover:underline"
                            href={link.href}
                            target="_blank"
                          >
                            {link.label}
                          </Link>
                        </li>
                      ))}
                    </ul>
                  </CardContent>
                </Card>
              ) : null}
            </div>
          </CardContent>
        ) : null}
      </Card>
    </div>
  )
}
