"use client";

import { Button } from "@/components/ui/button";
import { SheetFooter } from "@/components/ui/sheet";
import type { BikeDetailFooterProps } from "./bike-detail-sheet.types";

export function BikeDetailSheetFooter({
  bike,
  isLoading,
  errorMessage,
  isSuccess,
  onReserveClick,
}: BikeDetailFooterProps) {
  return (
    <SheetFooter>
      <div className="flex w-full flex-col gap-2">
        <Button
          onClick={onReserveClick}
          disabled={
            !bike || bike.status !== "AVAILABLE" || isLoading
          }
          className="w-full"
        >
          {isLoading
            ? "Reservando moto..."
            : bike.status === "AVAILABLE"
              ? "Reservar moto"
              : "No disponible para reservar"}
        </Button>

        {errorMessage && (
          <p className="text-sm text-red-600">{errorMessage}</p>
        )}

        {isSuccess && !errorMessage && (
          <p className="text-sm text-green-600">
            Moto reservada correctamente.
          </p>
        )}
      </div>
    </SheetFooter>
  );
}


