'use client'

import { TechnologyCategory } from '@/components/home/technology.types'
import { AppBreadcrumbs } from '@/components/shared/AppBreadcrumbs'
import { TechnologyModuleNavList } from '@/components/technology/TechnologyModuleNavList'
import { TechnologyModuleRenderer } from '@/components/technology/TechnologyModuleRenderer'
import {
  TechnologyModule,
  technologyModules,
} from '@/components/technology/technologyModules'
import { Badge } from '@/components/ui/badge'
import { Button } from '@/components/ui/button'
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card'
import { cn } from '@/lib/utils'
import {
  ChevronDown,
  ChevronLeft,
  ChevronRight,
  FolderTree,
} from 'lucide-react'
import { useEffect, useState } from 'react'

interface TechnologyWorkspaceProps {
  technology: TechnologyCategory
}

export const TechnologyWorkspace = ({
  technology,
}: TechnologyWorkspaceProps) => {
  const [isDesktopMenuCollapsed, setIsDesktopMenuCollapsed] = useState(false)
  const [isMobileModuleNavOpen, setIsMobileModuleNavOpen] = useState(false)
  const [selectedModule, setSelectedModule] = useState<TechnologyModule | null>(
    null,
  )
  const [isModuleReady, setIsModuleReady] = useState(false)

  useEffect(() => {
    const queryModule = new URLSearchParams(window.location.search).get(
      'module',
    )
    if (technologyModules.includes(queryModule as TechnologyModule)) {
      setSelectedModule(queryModule as TechnologyModule)
      setIsModuleReady(true)
      return
    }
    setSelectedModule('Interview Questions')
    setIsModuleReady(true)
  }, [])

  const onSelectModule = (module: TechnologyModule) => {
    setSelectedModule(module)
    const nextUrl = new URL(window.location.href)
    const nextParams = new URLSearchParams(nextUrl.search)
    nextParams.set('module', module)
    nextUrl.search = nextParams.toString()
    window.history.replaceState({}, '', nextUrl.toString())
    setIsMobileModuleNavOpen(false)
  }

  return (
    <main className="min-h-svh min-h-[100dvh] bg-background pb-[env(safe-area-inset-bottom,0px)]">
      <div className="flex min-h-0 w-full min-w-0 flex-1 flex-col lg:min-h-svh lg:flex-row">
        <aside
          className={cn(
            'z-20 flex w-full min-w-0 flex-shrink-0 flex-col border-b border-border/70 bg-card shadow-sm',
            'lg:sticky lg:top-2 lg:ml-2 lg:mt-2 lg:mb-2 lg:max-h-[min(100dvh-1rem,100svh)] lg:overflow-hidden lg:rounded-lg lg:border lg:shadow-sm',
            isDesktopMenuCollapsed ? 'lg:w-16' : 'lg:w-72',
          )}
        >
          <div className="flex min-h-12 items-center justify-between gap-2 border-b border-border/70 p-2 sm:p-3">
            <p className="min-w-0 flex-1 truncate pl-0.5 text-sm font-semibold">
              <span className="lg:hidden">{technology.title}</span>
              <span className="hidden lg:inline">
                {isDesktopMenuCollapsed ? null : technology.title}
              </span>
            </p>
            <Button
              aria-controls="technology-module-nav"
              aria-label="Toggle module menu width"
              className="hidden shrink-0 lg:inline-flex"
              onClick={() => setIsDesktopMenuCollapsed((p) => !p)}
              size="icon-sm"
              type="button"
              variant="ghost"
            >
              {isDesktopMenuCollapsed ? (
                <ChevronRight className="h-4 w-4" />
              ) : (
                <ChevronLeft className="h-4 w-4" />
              )}
            </Button>
          </div>

          {!isMobileModuleNavOpen && (
            <div className="border-t border-border/70 p-2 lg:hidden">
              <Button
                aria-controls="technology-module-nav"
                aria-expanded={isMobileModuleNavOpen}
                className="h-11 w-full min-w-0 justify-between gap-2 px-3"
                onClick={() => setIsMobileModuleNavOpen(true)}
                type="button"
                variant="outline"
              >
                <FolderTree className="h-4 w-4 shrink-0" aria-hidden />
                <span className="min-w-0 flex-1 truncate text-left text-sm font-medium">
                  {selectedModule ?? 'Select module'}
                </span>
                <ChevronDown className="h-4 w-4 shrink-0 opacity-70" />
              </Button>
            </div>
          )}

          {isModuleReady && selectedModule ? (
            <TechnologyModuleNavList
              isDesktopMenuCollapsed={isDesktopMenuCollapsed}
              isMobileModuleNavOpen={isMobileModuleNavOpen}
              onSelectModule={onSelectModule}
              selectedModule={selectedModule}
            />
          ) : null}
        </aside>

        <section className="min-w-0 flex-1 overflow-x-hidden px-3 py-4 sm:px-4 lg:p-6">
          <div className="mb-3 -mx-1 overflow-x-auto px-1 sm:mb-4 lg:mx-0 lg:px-0">
            <div className="min-w-0 rounded-lg bg-card p-3 sm:p-4">
              <AppBreadcrumbs
                items={[
                  { label: 'Technologies', href: '/' },
                  { label: technology.title, href: `/${technology.slug}` },
                  { label: selectedModule ?? 'Loading module...' },
                ]}
              />
            </div>
          </div>

          <Card className="min-w-0 max-w-full border-none">
            <CardHeader className="space-y-2 sm:space-y-3">
              <CardTitle className="break-words text-xl sm:text-2xl">
                {selectedModule ?? 'Loading module...'}
              </CardTitle>
              <div className="flex flex-wrap gap-1.5 sm:gap-2">
                <Badge
                  variant="secondary"
                  className="max-w-full truncate rounded-lg"
                >
                  Technology: {technology.title}
                </Badge>
                <Badge
                  variant="secondary"
                  className="max-w-full truncate rounded-lg"
                >
                  Questions: {technology.questionCount}
                </Badge>
                <Badge
                  variant="secondary"
                  className="max-w-full truncate rounded-lg"
                >
                  Exercises: {technology.exerciseCount}
                </Badge>
              </div>
            </CardHeader>
            <CardContent className="min-w-0 space-y-4">
              <div className="min-w-0 max-w-full overflow-x-hidden">
                {isModuleReady && selectedModule ? (
                  <TechnologyModuleRenderer
                    module={selectedModule}
                    technologySlug={technology.slug}
                  />
                ) : null}
              </div>
            </CardContent>
          </Card>
        </section>
      </div>
    </main>
  )
}
