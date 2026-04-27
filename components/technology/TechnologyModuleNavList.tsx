'use client'

import {
  TechnologyModule,
  technologyModules,
} from '@/components/technology/technologyModules'
import { cn } from '@/lib/utils'
import { FolderTree } from 'lucide-react'

interface TechnologyModuleNavListProps {
  isDesktopMenuCollapsed: boolean
  isMobileModuleNavOpen: boolean
  onSelectModule: (module: TechnologyModule) => void
  selectedModule: TechnologyModule
}

export const TechnologyModuleNavList = ({
  isDesktopMenuCollapsed,
  isMobileModuleNavOpen,
  onSelectModule,
  selectedModule,
}: TechnologyModuleNavListProps) => (
  <nav
    aria-label="Module navigation"
    className={cn(
      'min-h-0 flex-1 flex-col gap-1.5 overflow-y-auto overflow-x-hidden p-2',
      isMobileModuleNavOpen ? 'flex flex-col' : 'hidden',
      'lg:flex lg:flex-col',
      'lg:gap-0 lg:pb-2',
    )}
    id="technology-module-nav"
  >
    {technologyModules.map((module) => {
      const isActive = selectedModule === module
      return (
        <button
          className={cn(
            'flex min-h-11 w-full min-w-0 items-center justify-start gap-2 rounded-md border border-transparent px-3 py-2.5 text-left text-sm transition-colors',
            'active:bg-primary/10',
            isActive
              ? 'bg-primary text-white'
              : 'text-primary hover:border-primary hover:bg-muted/50',
            isDesktopMenuCollapsed ? 'lg:justify-center lg:px-2' : '',
          )}
          key={module}
          onClick={() => onSelectModule(module)}
          type="button"
        >
          <FolderTree className="h-4 w-4 shrink-0" aria-hidden />
          <span
            className={cn(
              'min-w-0 break-words text-left [overflow-wrap:anywhere] md:whitespace-nowrap',
              isDesktopMenuCollapsed ? 'md:sr-only' : '',
            )}
          >
            {module}
          </span>
        </button>
      )
    })}
  </nav>
)
