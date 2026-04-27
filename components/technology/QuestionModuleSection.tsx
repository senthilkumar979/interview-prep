'use client'

import { QuestionItem } from '@/components/technology/moduleData.types'
import { QuestionCard } from '@/components/technology/QuestionCard'
import { useMemo, useState } from 'react'

interface QuestionModuleSectionProps {
  items: QuestionItem[]
}

export const QuestionModuleSection = ({
  items,
}: QuestionModuleSectionProps) => {
  const [activeDifficulty, setActiveDifficulty] = useState<string | null>(null)
  const [sortBy, setSortBy] = useState<'none' | 'category' | 'difficulty'>(
    'none',
  )

  const difficulties = useMemo(
    () =>
      Array.from(
        new Set(
          items
            .map((item) => item.difficulty.trim().toLowerCase())
            .filter(Boolean),
        ),
      ),
    [items],
  )

  const filteredItems = useMemo(() => {
    if (!activeDifficulty) return items
    return items.filter(
      (item) => item.difficulty.trim().toLowerCase() === activeDifficulty,
    )
  }, [activeDifficulty, items])

  const sortedItems = useMemo(() => {
    if (sortBy === 'none') return filteredItems

    const difficultyOrder: Record<string, number> = {
      beginner: 1,
      intermediate: 2,
      advanced: 3,
      expert: 4,
    }

    return [...filteredItems].sort((left, right) => {
      if (sortBy === 'category')
        return left.category.localeCompare(right.category)

      const leftRank =
        difficultyOrder[left.difficulty.trim().toLowerCase()] ?? 999
      const rightRank =
        difficultyOrder[right.difficulty.trim().toLowerCase()] ?? 999
      if (leftRank !== rightRank) return leftRank - rightRank
      return left.category.localeCompare(right.category)
    })
  }, [filteredItems, sortBy])

  const getChipClass = (isActive: boolean) =>
    `rounded-full border px-3 py-1 text-xs font-medium transition-colors ${
      isActive
        ? 'border-primary bg-primary text-primary-foreground'
        : 'border-border bg-background text-muted-foreground hover:bg-muted'
    }`

  return (
    <div className="space-y-4">
      <div className="flex flex-col justify-between gap-3 md:flex-row md:items-start">
        <div className="rounded-lg border bg-card p-3 md:max-w-[48%] flex items-center justify-start gap-2">
          <p className="mb-0 text-sm font-semibold">Sort By:</p>
          <div className="flex flex-wrap gap-2 items-center justify-start">
            {[
              { key: 'none', label: 'None' },
              { key: 'category', label: 'Category' },
              { key: 'difficulty', label: 'Difficulty' },
            ].map((option) => (
              <button
                key={option.key}
                className={getChipClass(sortBy === option.key)}
                onClick={() =>
                  setSortBy(option.key as 'none' | 'category' | 'difficulty')
                }
                type="button"
              >
                {option.label}
              </button>
            ))}
          </div>
        </div>

        <div className="rounded-lg border bg-card p-3 md:max-w-[48%] flex items-center justify-start gap-2">
          <p className="mb-0 text-sm font-semibold">Filter By:</p>
          <div className="flex flex-wrap gap-2">
            <button
              className={getChipClass(activeDifficulty === null)}
              onClick={() => setActiveDifficulty(null)}
              type="button"
            >
              All
            </button>
            {difficulties.map((difficulty) => (
              <button
                key={difficulty}
                className={getChipClass(activeDifficulty === difficulty)}
                onClick={() =>
                  setActiveDifficulty((currentDifficulty) =>
                    currentDifficulty === difficulty ? null : difficulty,
                  )
                }
                type="button"
              >
                {difficulty.charAt(0).toUpperCase() + difficulty.slice(1)}
              </button>
            ))}
          </div>
        </div>
      </div>

      {sortedItems.length ? (
        sortedItems.map((item, index) => (
          <QuestionCard key={item.id} item={item} number={index + 1} />
        ))
      ) : (
        <p className="text-sm text-muted-foreground">
          No questions found for this difficulty.
        </p>
      )}
    </div>
  )
}
