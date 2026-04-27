'use client'

interface ControlOption {
  key: string
  label: string
}

interface FilterSortControlsProps {
  sortLabel?: string
  filterLabel?: string
  sortOptions: ControlOption[]
  filterOptions: ControlOption[]
  activeSort: string
  activeFilter: string | null
  onSortChange: (value: string) => void
  onFilterChange: (value: string | null) => void
}

const getChipClass = (isActive: boolean): string =>
  `rounded-full border px-3 py-1 text-xs font-medium transition-colors ${
    isActive
      ? 'border-primary bg-primary text-primary-foreground'
      : 'border-border bg-background text-muted-foreground hover:bg-muted'
  }`

export const FilterSortControls = ({
  sortLabel = 'Sort By:',
  filterLabel = 'Filter By:',
  sortOptions,
  filterOptions,
  activeSort,
  activeFilter,
  onSortChange,
  onFilterChange,
}: FilterSortControlsProps) => (
  <div className="flex flex-col justify-between gap-3 md:flex-row md:items-start">
    <div className="flex items-center justify-start gap-2 rounded-lg border bg-card p-3 md:max-w-[48%]">
      <p className="mb-0 text-sm font-semibold">{sortLabel}</p>
      <div className="flex flex-wrap items-center justify-start gap-2">
        {sortOptions.map((option) => (
          <button
            key={option.key}
            className={getChipClass(activeSort === option.key)}
            onClick={() => onSortChange(option.key)}
            type="button"
          >
            {option.label}
          </button>
        ))}
      </div>
    </div>

    <div className="flex items-center justify-start gap-2 rounded-lg border bg-card p-3 md:max-w-[48%]">
      <p className="mb-0 text-sm font-semibold">{filterLabel}</p>
      <div className="flex flex-wrap gap-2">
        {filterOptions.map((option) => {
          const isAllOption = option.key === 'all'
          const isActive = isAllOption
            ? activeFilter === null
            : activeFilter === option.key
          return (
            <button
              key={option.key}
              className={getChipClass(isActive)}
              onClick={() => onFilterChange(isAllOption ? null : option.key)}
              type="button"
            >
              {option.label}
            </button>
          )
        })}
      </div>
    </div>
  </div>
)
