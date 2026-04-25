'use client'

import { MarkdownContent } from '@/components/shared/MarkdownContent'
import { QuestionItem } from '@/components/technology/moduleData.types'
import { Badge } from '@/components/ui/badge'
import { Button } from '@/components/ui/button'
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card'
import { ChevronDown, ChevronUp, LinkIcon } from 'lucide-react'
import Link from 'next/link'
import { useState } from 'react'

interface QuestionCardProps {
  item: QuestionItem
  number: number
}

function getDifficultyBadgeClass(difficulty: string): string {
  const normalizedDifficulty = difficulty.toLowerCase()
  if (normalizedDifficulty === 'beginner') return 'difficulty-beginner'
  if (normalizedDifficulty === 'intermediate') return 'difficulty-intermediate'
  if (normalizedDifficulty === 'expert') return 'difficulty-expert'
  if (normalizedDifficulty === 'advanced') return 'difficulty-advanced'
  return 'border-border bg-muted text-muted-foreground'
}

function getCategoryBadgeClass(category: string): string {
  const normalizedCategory = category.toLowerCase()
  if (normalizedCategory === 'hooks') return 'category-hooks'
  if (normalizedCategory === 'state') return 'category-state'
  if (normalizedCategory === 'lifecycle') return 'category-lifecycle'
  if (normalizedCategory === 'performance') return 'category-performance'
  if (normalizedCategory === 'rendering') return 'category-rendering'
  if (normalizedCategory === 'architecture') return 'category-architecture'
  if (normalizedCategory === 'testing') return 'category-testing'
  return 'border-border bg-muted text-muted-foreground'
}

export const QuestionCard = ({ item, number }: QuestionCardProps) => {
  const [isExpanded, setIsExpanded] = useState(false)

  return (
    <div className="space-y-3">
      <Card>
        <CardHeader
          className="space-y-1 cursor-pointer"
          onClick={() => setIsExpanded((current) => !current)}
        >
          <CardTitle className="text-lg flex items-center justify-between">
            #{number}. {item.question}
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
              className={`px-2 py-1 text-xs font-medium ${getDifficultyBadgeClass(
                item.difficulty,
              )}`}
            >
              {item.difficulty}
            </Badge>
            <Badge
              className={`px-2 py-1 text-xs font-medium ${getCategoryBadgeClass(
                item.category,
              )}`}
            >
              {item.category}
            </Badge>
          </div>
        </CardHeader>
        {isExpanded ? (
          <CardContent className="space-y-4 text-sm">
            <Card>
              <CardHeader>
                <CardTitle className="text-base">Deep explanation</CardTitle>
              </CardHeader>
              <CardContent>
                <MarkdownContent content={item.answer} />
              </CardContent>
            </Card>

            <div className="flex flex-row items-start justify-between gap-4">
              {item.examples.map((example, index) => (
                <Card key={example.title}>
                  <CardHeader className="space-y-2">
                    <CardTitle className="text-base">
                      Code example #{index + 1}
                    </CardTitle>
                    <p className="text-xs text-muted-foreground">
                      {example.title}
                    </p>
                  </CardHeader>
                  <CardContent className="space-y-3">
                    <MarkdownContent
                      content={`\`\`\`${example.language}\n${example.code}\n\`\`\``}
                    />
                    <div className="rounded-md border border-border/70 bg-muted/30 p-3 text-sm text-muted-foreground">
                      {example.explanation}
                    </div>
                  </CardContent>
                </Card>
              ))}
            </div>

            <Card>
              <CardHeader>
                <CardTitle className="text-base">Tip</CardTitle>
              </CardHeader>
              <CardContent>
                <p
                  className="rounded-md border p-3 text-sm"
                  style={{
                    borderColor: '#8B5CF6',
                    backgroundColor: '#2E1065',
                    color: '#E9D5FF',
                  }}
                >
                  {item.tip}
                </p>
              </CardContent>
            </Card>

            {item.links?.length ? (
              <Card>
                <CardHeader>
                  <CardTitle className="text-base">Links</CardTitle>
                </CardHeader>
                <CardContent>
                  <ul className="list-disc space-y-1 pl-5">
                    {item.links.map((link) => (
                      <li
                        key={link.href}
                        className="cursor-pointer list-none flex items-center gap-2"
                      >
                        <LinkIcon className="h-3 w-3 text-primary" />
                        <Link
                          className="text-primary underline-offset-2 hover:underline"
                          href={link.href}
                        >
                          {link.label}
                        </Link>
                      </li>
                    ))}
                  </ul>
                </CardContent>
              </Card>
            ) : null}
          </CardContent>
        ) : null}
      </Card>
    </div>
  )
}
