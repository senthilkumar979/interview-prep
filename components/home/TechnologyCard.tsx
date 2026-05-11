import { TechnologyCategory } from '@/components/home/technology.types'
import { Card, CardContent, CardHeader } from '@/components/ui/card'
import { cn } from '@/lib/utils'
import {
  Atom,
  Braces,
  Coffee,
  Dumbbell,
  Layers3,
  ListChecks,
  LucideIcon,
  Sparkles,
} from 'lucide-react'
import Link from 'next/link'

const iconMap: Record<string, LucideIcon> = {
  angular: Layers3,
  java: Coffee,
  javascript: Braces,
  react: Atom,
}

interface TechnologyCardProps {
  technology: TechnologyCategory
}

export const TechnologyCard = ({ technology }: TechnologyCardProps) => {
  const Icon = iconMap[technology.icon] ?? Sparkles
  const { easy, medium, hard } = technology.difficultyBreakdown
  const totalDifficulty = easy + medium + hard || 1

  return (
    <Link
      href={`/${technology.slug}`}
      className="group block h-full rounded-xl focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 focus-visible:ring-offset-background"
    >
      <Card
        className={cn(
          'relative h-full gap-0 overflow-hidden border-border/60 bg-card py-0 shadow-sm transition-all duration-300',
          'hover:-translate-y-0.5 hover:border-primary/35 hover:shadow-md',
        )}
      >
        <div
          className="pointer-events-none absolute inset-x-0 top-0 h-1 bg-gradient-to-r from-primary/0 via-primary/70 to-primary/0 opacity-0 transition-opacity duration-300 group-hover:opacity-100"
          aria-hidden
        />

        <CardHeader className="gap-4 border-none border-border/50 bg-muted/25 px-5 pb-0 pt-5">
          <div className="flex items-start justify-start items-center gap-3">
            <div
              className={cn(
                'flex h-12 w-12 shrink-0 items-center justify-center rounded-xl border border-border/60 bg-background/80 text-muted-foreground shadow-sm',
                'transition-colors duration-300 group-hover:border-primary/25 group-hover:bg-primary/8 group-hover:text-primary',
              )}
            >
              <Icon className="h-6 w-6" aria-hidden />
            </div>
            <h2 className="font-heading text-xl font-semibold tracking-tight text-foreground">
              {technology.title}
            </h2>
          </div>
          <div className="space-y-1.5">
            <p className="line-clamp-3 text-sm leading-relaxed text-muted-foreground text-balance h-[70px]">
              {technology.description}
            </p>
          </div>
        </CardHeader>

        <CardContent className="space-y-4 px-5 py-5">
          <div className="grid grid-cols-2 gap-3">
            <div className="rounded-lg border border-border/50 bg-muted/20 px-3 py-2.5">
              <div className="flex items-center gap-1.5 text-[11px] font-medium uppercase tracking-wide text-muted-foreground">
                <ListChecks className="h-3.5 w-3.5" aria-hidden />
                Questions
              </div>
              <p className="mt-1 text-lg font-semibold tabular-nums tracking-tight">
                {technology.questionCount}
              </p>
            </div>
            <div className="rounded-lg border border-border/50 bg-muted/20 px-3 py-2.5">
              <div className="flex items-center gap-1.5 text-[11px] font-medium uppercase tracking-wide text-muted-foreground">
                <Dumbbell className="h-3.5 w-3.5" aria-hidden />
                Exercises
              </div>
              <p className="mt-1 text-lg font-semibold tabular-nums tracking-tight">
                {technology.exerciseCount}
              </p>
            </div>
          </div>

          <div className="space-y-2">
            <p className="text-[11px] font-medium uppercase tracking-wide text-muted-foreground">
              Difficulty mix
            </p>
            <div
              className="flex h-2.5 overflow-hidden rounded-full bg-muted"
              role="img"
              aria-label={`Difficulty: ${easy} easy, ${medium} medium, ${hard} hard`}
            >
              <span
                className="bg-emerald-500/85 dark:bg-emerald-400/90"
                style={{ width: `${(easy / totalDifficulty) * 100}%` }}
              />
              <span
                className="bg-amber-500/85 dark:bg-amber-400/90"
                style={{ width: `${(medium / totalDifficulty) * 100}%` }}
              />
              <span
                className="bg-rose-500/85 dark:bg-rose-400/90"
                style={{ width: `${(hard / totalDifficulty) * 100}%` }}
              />
            </div>
            <div className="flex flex-wrap gap-x-4 gap-y-1 text-xs text-muted-foreground">
              <span className="inline-flex items-center gap-1.5">
                <span className="h-2 w-2 rounded-full bg-emerald-500 dark:bg-emerald-400" />
                Easy {easy}
              </span>
              <span className="inline-flex items-center gap-1.5">
                <span className="h-2 w-2 rounded-full bg-amber-500 dark:bg-amber-400" />
                Med {medium}
              </span>
              <span className="inline-flex items-center gap-1.5">
                <span className="h-2 w-2 rounded-full bg-rose-500 dark:bg-rose-400" />
                Hard {hard}
              </span>
            </div>
          </div>
        </CardContent>

        {/* <CardFooter className="border-t border-border/50 bg-muted/15 px-5 py-3 text-xs text-muted-foreground">
          <span className="truncate">
            Interview prep ·{' '}
            <span className="text-foreground/80">{technology.title}</span>
          </span>
        </CardFooter> */}
      </Card>
    </Link>
  )
}
