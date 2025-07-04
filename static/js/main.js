// Main JavaScript file for RealEstate website

document.addEventListener("DOMContentLoaded", () => {
  // Initialize tooltips
  var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
  var tooltipList = tooltipTriggerList.map((tooltipTriggerEl) => new window.bootstrap.Tooltip(tooltipTriggerEl))

  // Initialize popovers
  var popoverTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="popover"]'))
  var popoverList = popoverTriggerList.map((popoverTriggerEl) => new window.bootstrap.Popover(popoverTriggerEl))

  // Smooth scrolling for anchor links
  document.querySelectorAll('a[href^="#"]').forEach((anchor) => {
    anchor.addEventListener("click", function (e) {
      e.preventDefault()
      const target = document.querySelector(this.getAttribute("href"))
      if (target) {
        target.scrollIntoView({
          behavior: "smooth",
          block: "start",
        })
      }
    })
  })

  // Property card animations
  const observerOptions = {
    threshold: 0.1,
    rootMargin: "0px 0px -50px 0px",
  }

  const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add("fade-in-up")
      }
    })
  }, observerOptions)

  // Observe property cards
  document.querySelectorAll(".property-card, .agent-card").forEach((card) => {
    observer.observe(card)
  })

  // Search form enhancements
  const searchForm = document.querySelector(".search-card form")
  if (searchForm) {
    // Auto-submit on filter change (optional)
    const autoSubmitElements = searchForm.querySelectorAll("select[data-auto-submit]")
    autoSubmitElements.forEach((element) => {
      element.addEventListener("change", () => {
        searchForm.submit()
      })
    })
  }

  // Price range formatting
  const priceInputs = document.querySelectorAll('input[name="min_price"], input[name="max_price"]')
  priceInputs.forEach((input) => {
    input.addEventListener("input", function () {
      // Format number with commas
      const value = this.value.replace(/,/g, "")
      if (value && !isNaN(value)) {
        this.value = Number.parseInt(value).toLocaleString()
      }
    })
  })

  // Loading states for buttons
  document.querySelectorAll('button[type="submit"]').forEach((button) => {
    button.addEventListener("click", function () {
      if (this.form && this.form.checkValidity()) {
        this.classList.add("loading")
        this.disabled = true

        // Re-enable after 3 seconds (fallback)
        setTimeout(() => {
          this.classList.remove("loading")
          this.disabled = false
        }, 3000)
      }
    })
  })

  // Image lazy loading fallback
  const images = document.querySelectorAll("img[data-src]")
  const imageObserver = new IntersectionObserver((entries, observer) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        const img = entry.target
        img.src = img.dataset.src
        img.classList.remove("lazy")
        imageObserver.unobserve(img)
      }
    })
  })

  images.forEach((img) => imageObserver.observe(img))

  // Contact form handling
  const contactForms = document.querySelectorAll(".contact-form")
  contactForms.forEach((form) => {
    form.addEventListener("submit", (e) => {
      e.preventDefault()

      // Basic form validation
      const requiredFields = form.querySelectorAll("[required]")
      let isValid = true

      requiredFields.forEach((field) => {
        if (!field.value.trim()) {
          field.classList.add("is-invalid")
          isValid = false
        } else {
          field.classList.remove("is-invalid")
        }
      })

      if (isValid) {
        // Submit form (you can add AJAX here)
        form.submit()
      }
    })
  })

  // Navbar scroll effect
  const navbar = document.querySelector(".navbar")
  if (navbar) {
    window.addEventListener("scroll", () => {
      if (window.scrollY > 100) {
        navbar.classList.add("scrolled")
      } else {
        navbar.classList.remove("scrolled")
      }
    })
  }

  // Back to top button
  const backToTopButton = document.createElement("button")
  backToTopButton.innerHTML = '<i class="fas fa-arrow-up"></i>'
  backToTopButton.className = "btn btn-primary btn-floating back-to-top"
  backToTopButton.style.cssText = `
        position: fixed;
        bottom: 20px;
        right: 20px;
        z-index: 1000;
        border-radius: 50%;
        width: 50px;
        height: 50px;
        display: none;
        box-shadow: 0 4px 12px rgba(0,0,0,0.15);
    `

  document.body.appendChild(backToTopButton)

  window.addEventListener("scroll", () => {
    if (window.scrollY > 300) {
      backToTopButton.style.display = "block"
    } else {
      backToTopButton.style.display = "none"
    }
  })

  backToTopButton.addEventListener("click", () => {
    window.scrollTo({
      top: 0,
      behavior: "smooth",
    })
  })
})

// Utility functions
function formatPrice(price) {
  return "₦" + Number.parseInt(price).toLocaleString()
}

function showNotification(message, type = "info") {
  // Create notification element
  const notification = document.createElement("div")
  notification.className = `alert alert-${type} alert-dismissible fade show position-fixed`
  notification.style.cssText = "top: 20px; right: 20px; z-index: 9999; min-width: 300px;"
  notification.innerHTML = `
        ${message}
        <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
    `

  document.body.appendChild(notification)

  // Auto remove after 5 seconds
  setTimeout(() => {
    if (notification.parentNode) {
      notification.remove()
    }
  }, 5000)
}

// Export functions for use in other scripts
window.RealEstate = {
  formatPrice,
  showNotification,
}
