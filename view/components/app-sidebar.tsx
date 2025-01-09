"use client"

import * as React from "react"
import {
  AudioWaveform,
  GalleryVerticalEnd,
  LayoutDashboard,
  ChartCandlestick,
  HandCoins,
  ChartNoAxesCombined,
  CircleDollarSign,
  Building2,
  Bitcoin,
  Flame,
  Star
} from "lucide-react"

import { NavMain } from "@/components/nav-main"
import { NavProjects } from "@/components/nav-projects"
import { NavUser } from "@/components/nav-user"
import { TickerSwitcher } from "@/components/ticker-switcher"
import {
  Sidebar,
  SidebarContent,
  SidebarFooter,
  SidebarHeader,
  SidebarRail,
} from "@/components/ui/sidebar"

// This is sample data.
const data = {
  user: {
    name: "alexandria",
    email: "hello@alexandria.ventari.id",
    avatar: "assets/avatars/avatar2.jpeg",
  },
  tickers: [
    {
      name: "ADRO",
      symbol: "ADRO.JK",
      companyName: "PT Alamtri Resources Indonesia Tbk",
      logo: ChartCandlestick,
      plan: "Enterprise",
    },
    {
      name: "BBCA",
      symbol: "BBCA.JK",
      companyName: "PT Bank Central Asia Tbk",
      logo: GalleryVerticalEnd,
      plan: "Enterprise",
    },
    {
      name: "PTBA",
      symbol: "PTBA.JK",
      companyName: "PT Bukit Asam Tbk",
      logo: AudioWaveform,
      plan: "Startup",
    },
      ],
  navMain: [
    {
      title: "Dashboard",
      url: "dashboard",
      icon: LayoutDashboard,
      isActive: true,
      items: [
      ],
    },
    {
      title: "Financial",
      url: "#",
      icon: CircleDollarSign,
      isActive: true,
      items: [
        {
          title: "Income Statement",
          url: "#",
        },
        {
          title: "Balance Sheet",
          url: "#",
        },
        {
          title: "Cash Flow",
          url: "#",
        },
      ],
    },
    {
      title: "Analysis",
      url: "#",
      icon: ChartNoAxesCombined,
      items: [
        {
          title: "Genesis",
          url: "#",
        },
        {
          title: "Explorer",
          url: "#",
        },
        {
          title: "Quantum",
          url: "#",
        },
      ],
    },
    {
      title: "Dividend",
      url: "#",
      icon: HandCoins,
      items: [
        {
          title: "Introduction",
          url: "#",
        },
        {
          title: "Get Started",
          url: "#",
        },
        {
          title: "Tutorials",
          url: "#",
        },
        {
          title: "Changelog",
          url: "#",
        },
      ],
    },
    {
      title: "Profile",
      url: "#",
      icon: Building2,
      items: [
        {
          title: "General",
          url: "#",
        },
        {
          title: "Team",
          url: "#",
        },
        {
          title: "Billing",
          url: "#",
        },
        {
          title: "Limits",
          url: "#",
        },
      ],
    },
  ],
  projects: [
    {
      name: "Coins",
      url: "#",
      icon: Bitcoin,
    },
    {
      name: "Trending",
      url: "#",
      icon: Flame,
    },
    {
      name: "Top Stories",
      url: "#",
      icon: Star,
    },
  ],
}

export function AppSidebar({ ...props }: React.ComponentProps<typeof Sidebar>) {
  return (
    <Sidebar collapsible="icon" {...props}>
      <SidebarHeader>
        <NavUser user={data.user} />
        <TickerSwitcher tickers={data.tickers} />
      </SidebarHeader>
      <SidebarContent>
        <NavMain items={data.navMain} />
        <NavProjects projects={data.projects} />
      </SidebarContent>
      <SidebarFooter>
      </SidebarFooter>
      <SidebarRail />
    </Sidebar>
  )
}

