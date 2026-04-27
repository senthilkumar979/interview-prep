import { useMemo } from 'react'

interface UseModuleFilterSortProps<TItem> {
  items: TItem[]
  activeFilter: string | null
  activeSort: string
  filterFn: (item: TItem, activeFilter: string | null) => boolean
  sorters: Record<string, (left: TItem, right: TItem) => number>
}

export function useModuleFilterSort<TItem>({
  items,
  activeFilter,
  activeSort,
  filterFn,
  sorters,
}: UseModuleFilterSortProps<TItem>): TItem[] {
  return useMemo(() => {
    const filteredItems = items.filter((item) => filterFn(item, activeFilter))
    const sorter = sorters[activeSort]
    if (!sorter) return filteredItems
    return [...filteredItems].sort(sorter)
  }, [activeFilter, activeSort, filterFn, items, sorters])
}
