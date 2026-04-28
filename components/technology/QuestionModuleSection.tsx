'use client'

import { FilterSortControls } from '@/components/technology/FilterSortControls'
import { QuestionItem } from '@/components/technology/moduleData.types'
import { QuestionCard } from '@/components/technology/QuestionCard'
import { useModuleFilterSort } from '@/components/technology/useModuleFilterSort'
import { useMemo, useState } from 'react'

interface QuestionModuleSectionProps {
  items: QuestionItem[]
}

export const QuestionModuleSection = ({
  items: itemsProp,
}: QuestionModuleSectionProps) => {
  const items = useMemo(
    () => (Array.isArray(itemsProp) ? itemsProp : []),
    [itemsProp],
  )
  const [activeDifficulty, setActiveDifficulty] = useState<string | null>(null)
  const [sortBy, setSortBy] = useState<'none' | 'category' | 'difficulty'>(
    'none',
  )

  const difficultyOptions = useMemo(
    () => [
      { key: 'all', label: 'All' },
      ...Array.from(
        new Set(
          items
            .map((item) => item.difficulty.trim().toLowerCase())
            .filter(Boolean),
        ),
      ).map((difficulty) => ({
        key: difficulty,
        label: difficulty.charAt(0).toUpperCase() + difficulty.slice(1),
      })),
    ],
    [items],
  )

  const sortOptions = useMemo(
    () => [
      { key: 'none', label: 'None' },
      { key: 'category', label: 'Category' },
      { key: 'difficulty', label: 'Difficulty' },
    ],
    [],
  )

  const sorters = useMemo(
    () => ({
      category: (left: QuestionItem, right: QuestionItem) =>
        left.category.localeCompare(right.category),
      difficulty: (left: QuestionItem, right: QuestionItem) => {
        const difficultyOrder: Record<string, number> = {
          beginner: 1,
          intermediate: 2,
          advanced: 3,
          expert: 4,
        }
        const leftRank =
          difficultyOrder[left.difficulty.trim().toLowerCase()] ?? 999
        const rightRank =
          difficultyOrder[right.difficulty.trim().toLowerCase()] ?? 999
        if (leftRank !== rightRank) return leftRank - rightRank
        return left.category.localeCompare(right.category)
      },
    }),
    [],
  )

  const visibleItems = useModuleFilterSort({
    items,
    activeFilter: activeDifficulty,
    activeSort: sortBy,
    filterFn: (item, filterValue) =>
      !filterValue || item.difficulty.trim().toLowerCase() === filterValue,
    sorters,
  })

  return (
    <div className="space-y-4">
      <FilterSortControls
        activeFilter={activeDifficulty}
        activeSort={sortBy}
        filterOptions={difficultyOptions}
        onFilterChange={setActiveDifficulty}
        onSortChange={(value) =>
          setSortBy(value as 'none' | 'category' | 'difficulty')
        }
        sortOptions={sortOptions}
      />

      {visibleItems.length ? (
        visibleItems.map((item, index) => (
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
