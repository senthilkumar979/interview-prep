import { KataItem } from '@/components/technology/moduleData.types'
import { Badge } from '@/components/ui/badge'
import { Button } from '@/components/ui/button'
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card'
import {
  CheckCircle2,
  ChevronDown,
  ChevronUp,
  Code2,
  FolderCode,
  Hammer,
} from 'lucide-react'
import { useState } from 'react'

interface KataChallengeCardProps {
  item: KataItem
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

export const KataChallengeCard = ({ item, number }: KataChallengeCardProps) => {
  const [isExpanded, setIsExpanded] = useState(false)

  return (
    <Card className={isExpanded ? 'border-2' : 'border-none'}>
      <CardHeader
        className="cursor-pointer space-y-2"
        onClick={() => setIsExpanded((current) => !current)}
      >
        <CardTitle className="flex items-center justify-between gap-3 text-lg">
          <div className="flex min-w-0 items-center gap-2">
            <Hammer className="h-4 w-4 shrink-0" />
            <span className="truncate">
              #{number}. {item.title}
            </span>
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
            className={`rounded-lg px-2 py-1 text-xs font-medium capitalize tracking-wide ${getDifficultyBadgeClass(
              item.difficulty,
            )}`}
          >
            {item.difficulty}
          </Badge>
          <Badge
            className={`rounded-lg px-2 py-1 text-xs font-medium capitalize tracking-wide ${getCategoryBadgeClass(
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
              <CardTitle className="text-base uppercase tracking-wide">
                <CheckCircle2 className="h-4 w-4" />
                Description
              </CardTitle>
            </CardHeader>
            <CardContent>
              <p className="text-muted-foreground">{item.description}</p>
            </CardContent>
          </Card>

          <Card className="border-none bg-muted">
            <CardHeader>
              <CardTitle className="text-base uppercase tracking-wide">
                <Code2 className="h-4 w-4" />
                Requirements
              </CardTitle>
            </CardHeader>
            <CardContent>
              <ul className="space-y-2 text-muted-foreground">
                {item.requirements.map((requirement) => (
                  <li key={requirement} className="flex items-start gap-2">
                    <CheckCircle2 className="mt-0.5 h-4 w-4 shrink-0 text-primary" />
                    <span>{requirement}</span>
                  </li>
                ))}
              </ul>
            </CardContent>
          </Card>

          <Card className="border-none bg-muted">
            <CardHeader>
              <CardTitle className="text-base uppercase tracking-wide">
                <FolderCode className="h-4 w-4" />
                Starter and solution files
              </CardTitle>
            </CardHeader>
            <CardContent className="space-y-2">
              <p className="rounded-md border border-border/70 bg-background px-3 py-2 font-mono text-xs">
                Starter: {item.starterCode}
              </p>
              <p className="rounded-md border border-border/70 bg-background px-3 py-2 font-mono text-xs">
                Solution: {item.solution}
              </p>
            </CardContent>
          </Card>
        </CardContent>
      ) : null}
    </Card>
  )
}
